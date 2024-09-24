import classNames from "classnames/bind";
import styles from "./Header.module.scss";
import UserTag from "../UserTag/UserTag";

const cx = classNames.bind(styles);

function Header() {
  return (
    <div className={cx("wrapper")}>
      <div className={cx("user")}>
        <UserTag index={1} />
        <UserTag index={2} position="right" />
      </div>
    </div>
  );
}

export default Header;
