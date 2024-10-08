import classNames from "classnames/bind";
import styles from "./SideBar.module.scss";
import Input from "../Input";

const cx = classNames.bind(styles);

function SideBar() {
  return (
    <div className={cx("wrapper")}>
      {/* <FontAwesomeIcon className={cx("icon")} icon={faCaretLeft} /> */}
      <div className={cx("input")}>
        <Input placeholder="Find id" />
      </div>
    </div>
  );
}

export default SideBar;
