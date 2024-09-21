import classNames from "classnames/bind";
import styles from "./Input.module.scss"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGlassCheers, faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";

const cx = classNames.bind(styles)

function Input({placeholder = '', type = 'text'}) {
    return <div className={cx('wrapper')}>
        <FontAwesomeIcon className={cx('icon')} icon={faMagnifyingGlass}/>
        <input type={type} placeholder={placeholder}/>
    </div>;
}

export default Input;