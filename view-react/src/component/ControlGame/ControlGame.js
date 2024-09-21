import classnames from "classnames/bind";
import styles from "./ControlGame.module.scss";

import {
  faCaretDown,
  faCaretLeft,
  faCaretRight,
  faCaretUp,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const cx = classnames.bind(styles);

function ControlGame({currentUser,  position, handleClick }) {

  // console.log(currentUser)

  return (
    <div className={cx("wrapper", position)}>
      {position === "left" ? (
        <>
          <div className={cx("left_left")}>
            <div className={cx("item")} onClick={()=>handleClick("top")}>
              <FontAwesomeIcon className={cx("icon")} icon={faCaretUp} />
            </div>
            <div className={cx("item")} onClick={()=>handleClick("down")}>
              <FontAwesomeIcon className={cx("icon")} icon={faCaretDown} />
            </div>
          </div>
          <div className={cx("left_right")}>
            <div className={cx("item")} onClick={()=>handleClick("right")}>
              <FontAwesomeIcon className={cx("icon")} icon={faCaretRight} />
            </div>
          </div>
        </>
      ) : (
        <>
          <div className={cx("bottom_top")}>
            <div className={cx("item")} onClick={()=>handleClick("top")}>
              <FontAwesomeIcon className={cx("icon")} icon={faCaretUp} />
            </div>
          </div>
          <div className={cx("bottom_bottom")}>
            <div className={cx("item")} onClick={()=>handleClick("left")}>
              <FontAwesomeIcon className={cx("icon")} icon={faCaretLeft} />
            </div>
            <div className={cx("item")} onClick={()=>handleClick("right")}>
              <FontAwesomeIcon className={cx("icon")} icon={faCaretRight} />
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default ControlGame;
