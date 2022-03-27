function firstUniqueProduct(products) {
  // Your code goes here
  const first = new Set();
  const twice = new Set();

  for (const el of products) {
    if (twice.has(el)) continue;
    if (first.has(el)) {
      first.delete(el);
      twice.add(el);
    } else {
      first.add(el);
    }
  }
  return first.size ? [...first][0] : null;
}

console.log(firstUniqueProduct(["Apple", "Computer", "Apple", "Bag"]));
