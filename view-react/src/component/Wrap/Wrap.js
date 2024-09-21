import classNames from "classnames/bind";
import styles from "./Wrap.module.scss";

const cx = classNames.bind(styles)

function Wrapp({children}) {
    return <div className={cx('wrapper')}>
        {children}
    </div>;
}

export default Wrapp;