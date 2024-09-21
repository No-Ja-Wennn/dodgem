import classNames from "classnames/bind";
import styles from "./UserTag.module.scss";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { useContext } from "react";

import { currentUserContext } from "../../App";

const cx = classNames.bind(styles);

function UserTag({position = 'left', index}) {
  const {currentUser} = useContext(currentUserContext);

  return (
    <div className={cx("wrapper", position)}>
      <h3 className={cx("usename", {'active': currentUser === index})}>post man</h3>
      <div className={cx("img")}>
        <FontAwesomeIcon icon={faUser} />
      </div>
      <span className={cx('couter')}>0</span>
    </div>
  );
}

export default UserTag;
