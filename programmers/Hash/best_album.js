function solution(genres, plays) {
  var dic = {};
  genres.forEach((t, i) => {
    // dictionary에 장르별로 재생 횟수 저장 (공통)
    dic[t] = dic[t] ? dic[t] + plays[i] : plays[i];
  });

  var dupDic = {};
  return (
    genres
      // 각 장르별로 장르명, 재생 수, 인덱스 설정
      .map((t, i) => ({ genre: t, count: plays[i], index: i }))
      .sort((a, b) => {
        // 노래 수록 기준으로 sorting
        // 1. 속한 노래 만이 재생된 장르 먼저 수록
        // 2. 장르 내에서 많이 재생된 노래 수록
        if (a.genre !== b.genre) return dic[b.genre] - dic[a.genre];
        if (a.count !== b.count) return b.count - a.count;
        return a.index - b.index;
      })
      // 그리고 중복되는 장르가 있으면 상위 두 개만 뽑는다.
      // dupDic의 용도: filter할 때 한 장르 안에서 3개 이상의 t(track)이 나오면
      // 상위 2개를 제외한 그 뒤의 track를 false해서 filtering하기 위함
      .filter((t) => {
        if (dupDic[t.genre] >= 2) return false;
        dupDic[t.genre] = dupDic[t.genre] ? dupDic[t.genre] + 1 : 1;
        return true;
      })
      // 같은 장르에 같은 재생횟수는 index로 정렬
      .map((t) => t.index)
  );
}

// 나의 풀이
function solution(genres, plays) {
  var answer = [];
  var gen_map = new Map();

  for (let i = 0; i < genres.length; i++) {
    const play = plays[i];
    const genre = genres[i];

    if (gen_map.get(genre)) {
      gen_map.set(genre, {
        total: gen_map.get(genre).total + play,
        gen_index: [...gen_map.get(genre).gen_index, { play, index: i }],
      });
    } else {
      gen_map.set(genre, {
        total: play,
        gen_index: [
          {
            play,
            index: i,
          },
        ],
      });
    }
  }

  let gen_arr = [...gen_map.values()].sort((a, b) => b.total - a.total);

  for (let i = 0; i < gen_arr.length; i++) {
    gen_arr[i].gen_index = gen_arr[i].gen_index.sort((x, y) => y.play - x.play);
    for (let j = 0; j < Math.min(2, gen_arr[i].gen_index.length); j++) {
      answer.push(gen_arr[i].gen_index[j].index);
    }
  }

  return answer;
}
