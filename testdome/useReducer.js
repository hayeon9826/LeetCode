// React is loaded and is available as React and ReactDOM
// imports should NOT be used
const OPERATIONS = {
  ADD: "ADD",
  SUBTRACT: "SUBTRACT",
};

function App() {
  const [number, updateNumber] = React.useState(0);

  const [state, dispatch] = React.useReducer((state, action) => {
    /* implement the reducer which should update the state based on the action */
    const resultDiv = document.querySelector("#root");

    console.log(number);
    console.log(state);

    switch (action.type) {
      case "ADD":
        return (state += number);
      case "SUBTRACT":
        return (state -= number);
        break;
    }

    resultDiv.innerHTML = state;

    return state;
  }, 0);

  /* implement dispatches */
  const add = () => dispatch({ type: "ADD" });
  const subtract = () => dispatch({ type: "SUBTRACT" });

  const handleNumberChange = (e) => updateNumber(Number(e.target.value));

  return (
    <div>
      <div id="result">{state}</div>
      <div>
        <button id="add" onClick={add}>
          Add
        </button>
        <button id="subtract" onClick={subtract}>
          Subtract
        </button>
      </div>
      <div>
        <input type="text" value={number} onChange={handleNumberChange} />
      </div>
    </div>
  );
}

document.body.innerHTML = "<div id='root'></div>";
const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
