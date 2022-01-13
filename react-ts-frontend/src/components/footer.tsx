import React from "react";
import styles from '../styles/footer.module.css';

const Footer: React.FC = () => {
    return (
        <div className={styles.footer}>
            <p style={{ paddingLeft: '10px' }}>React front end for PRI information retrieval project by Nuno Marques, Rodrigo Abrantes and Nuno Santos</p>
        </div>
    );
};

export default Footer;
