import Footer from '../components/footer';
import styles from '../styles/page.module.css';

interface props {
    children: React.ReactNode;
}

const PageLayout: React.FC<props> = (props: props) => {


    return (
        <div>
            <h1 style={{ textAlign: 'center' }}>Wine Reviews</h1>
            <main className={styles.main}>{props.children}</main>
            <Footer />
        </div>
    );

};

export default PageLayout;