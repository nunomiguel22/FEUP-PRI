import React from 'react';
import Footer from '../components/footer';
import styles from '../styles/page.module.css';

interface props {
    children: React.ReactNode;
}

const PageLayout: React.FC<props> = (props: props) => {


    return (
        <div>
            <main className={styles.main}>{props.children}</main>
            <Footer />
        </div>
    );

};

export default PageLayout;