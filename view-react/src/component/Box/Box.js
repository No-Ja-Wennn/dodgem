import classNames from "classnames/bind";
import styles from "./Box.module.scss";

const cx = classNames.bind(styles);

function Box({value, onClick, active, curStep}) {

    return <div className={cx('wrapper', {active, curStep})} onClick={onClick}>
        {value}
    </div>;
}

export default Box;