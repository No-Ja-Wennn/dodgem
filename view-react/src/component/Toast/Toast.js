import classNames from "classnames/bind";
import styles from "./Toast.module.scss";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCheck, faXmark } from "@fortawesome/free-solid-svg-icons";
import { useEffect, useState } from "react";

const cx = classNames.bind(styles);

function Toast({
  stateValue = "success",
  value = "This is a success message",
  onClose = ()=>{},
}) {
  const [hide, setHide] = useState(false);
  useEffect(() => {
    const timer = setTimeout(() => {
      setHide(true);
      setTimeout(onClose(), 500);
    }, 1000);
    return () => clearTimeout(timer);
  }, [onClose]);

  return (
    <div className={cx("wrapper", { [stateValue]: stateValue }, { hide: hide })}>
      <FontAwesomeIcon className={cx("icon", {[stateValue]: stateValue })} icon={faCheck} />
      <span className={cx("message")}>{value}</span>
      <FontAwesomeIcon className={cx("exit")} icon={faXmark} />
    </div>
  );
}

export default Toast;
