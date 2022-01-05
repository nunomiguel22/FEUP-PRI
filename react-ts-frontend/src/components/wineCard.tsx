import { Wine } from '../interfaces';
import styles from '../styles/winecard.module.css';

interface Props {
    wine: Wine;
}

const WineCard: React.FC<Props> = ({ wine }: Props) => {
    return (
        <div className={styles.cardStyle}>
            <p>{wine.name}</p>
            <p>{wine.year}</p>
            <img src={wine.image_url} alt="Wine" />
        </div>
    );
};

export default WineCard;
