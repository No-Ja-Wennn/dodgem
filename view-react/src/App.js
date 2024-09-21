import "./App.css";
import Box from "./component/Box/Box";
import Wrapp from "./component/Wrap/Wrap";
import { createContext, useEffect, useState } from "react";

import ControlGame from "./component/ControlGame";
import Header from "./component/Header";
// import SideBar from "./component/SideBar";
import Toast from "./component/Toast/Toast";

const x = "X";
const o = "O";
const empty = "";


export const currentUserContext = createContext();

function App() {
  const [values, setValues] = useState([
    [x, empty, empty],
    [x, empty, empty],
    [empty, o, o],
  ]);
  const [currentActive, setCurrentActive] = useState({
    rowIndex: null,
    colIndex: null,
  });
  const [toast, setToast] = useState({});
  const [currentUser, setCurrentUser] = useState(1);
  const [isError, setIsError] = useState(false);

  useEffect(() => {
    document.title = "Dodgen"; // Đặt tiêu đề
  }, []);

  useEffect(() => {
    if (!isError) {
      setCurrentUser((prevUser) => (prevUser === 1 ? 2 : 1));
      setCurrentActive({ rowIndex: null, colIndex: null });
    } else {
      addToast("warning", "Nước đi không đúng");
      setIsError(false);
    }
  }, [values]); 

  const addToast = (state, message) => {
    setToast({ message, state });
  };

  const removeToast = () => {
    setToast({});
  };

  const handleActiveBox = (rowIndex, colIndex) => {
    const currentTic = currentUser === 1 ? x : o;
    if(values[rowIndex][colIndex] === empty) return
    else if(currentTic !== values[rowIndex][colIndex])
      addToast("warning", "Đang tới lượt " + currentTic);
    else if (values[rowIndex][colIndex] !== empty)
      setCurrentActive({ rowIndex, colIndex });
  };

  const handleSetValues = (prev, position) => {
    const newValues = prev.map((row) => [...row]);
    const { rowIndex, colIndex } = currentActive;

    switch (position) {
      case "right":
        if (
          colIndex >= newValues[rowIndex].length - 1 &&
          newValues[rowIndex][colIndex] === x
        ) {
          newValues[rowIndex][colIndex] = empty;
        } else if (newValues[rowIndex][colIndex + 1] !== empty) {
          setIsError(true);
        } else {
          newValues[rowIndex][colIndex + 1] = newValues[rowIndex][colIndex];
          newValues[rowIndex][colIndex] = empty;
        }
        break;

      case "left":
        if (
          newValues[rowIndex][colIndex] !== o ||
          newValues[rowIndex][colIndex - 1] !== empty
        ) {
          setIsError(true);
        } else if (colIndex > 0) {
          newValues[rowIndex][colIndex - 1] = newValues[rowIndex][colIndex];
          newValues[rowIndex][colIndex] = empty;
        }
        break;

      case "down":
        if (
          newValues[rowIndex][colIndex] !== x ||
          !newValues[rowIndex + 1] ||
          newValues[rowIndex + 1][colIndex] !== empty
        ) {
          setIsError(true);
        } else if (rowIndex < newValues.length - 1) {
          newValues[rowIndex + 1][colIndex] = newValues[rowIndex][colIndex];
          newValues[rowIndex][colIndex] = empty;
        }
        break;

      case "top":
        if (!newValues[rowIndex - 1] && newValues[rowIndex][colIndex] === o) {
          newValues[rowIndex][colIndex] = empty;
        } else if (
          !newValues[rowIndex - 1] ||
          newValues[rowIndex - 1][colIndex] !== empty
        ) {
          setIsError(true);
        } else if (rowIndex <= 0) {
          newValues[rowIndex][colIndex] = empty;
        } else {
          newValues[rowIndex - 1][colIndex] = newValues[rowIndex][colIndex];
          newValues[rowIndex][colIndex] = empty;
        }
        break;

      default:
        break;
    }

    return newValues;
  };

  const handleClickControl = (position) => {
    if (currentActive.rowIndex === null || currentActive.colIndex === null) {
      addToast("warning", "Vui lòng chọn quân cờ");
      return;
    }
    const rowIndex = currentActive.rowIndex;
    const colIndex = currentActive.colIndex;

    if((currentUser === 1 ? x : o ) === values[rowIndex][colIndex]){
      console.log("hop ly")
      setValues((prev) => handleSetValues(prev, position));
    }else{
      addToast("warning", "Chọn sai quân");
    }


  };

  return (
    <div className="App">
      <currentUserContext.Provider value={{ currentUser }}>
        
      <Header />
      <div className="container">
        <div className="toast">
          {Object.keys(toast).length > 0 && (
            <Toast
              stateValue={toast.state}
              value={toast.message}
              onClose={() => removeToast()}
            />
          )}
        </div>
        <Wrapp>
          {values.map((row, rowIndex) =>
            row.map((col, colIndex) => (
              <Box
                active={
                  currentActive.rowIndex === rowIndex &&
                  currentActive.colIndex === colIndex
                    ? "active"
                    : ""
                }
                value={col}
                curStep = {(currentUser === 1 ? x : o) === col}
                key={`${rowIndex}-${colIndex}`}
                onClick={() => handleActiveBox(rowIndex, colIndex)}
              />
            ))
          )}
        </Wrapp>
        <ControlGame
          currentUser={currentUser}
          // active={currentUser === 1}
          position={currentUser === 1 ? "left" : "bottom"}
          handleClick={handleClickControl}
        />
        {/* <ControlGame
          active={currentUser === 2}
          position="bottom"
          handleClick={handleClickControl}
        /> */}
      </div>
      </currentUserContext.Provider>
    </div>
  );
}

export default App;
