import { Wine } from '../interfaces';
import styles from '../styles/winecard.module.css';
import { Link } from "react-router-dom";
import Rating from 'react-rating';

interface Props {
    wine: Wine;
}

const WineCard: React.FC<Props> = ({ wine }: Props) => {
    return (
        <Link className={styles.cardStyle} to={'/wine/' + wine.id}>
            <div className={styles.cardHalf}>
                <h5 style={{ color: '#616161' }}>{wine.winery}</h5>
                <h3>{wine.name}</h3>
                <p style={{ fontSize: '17px' }}>{wine.region}</p>
                <p style={{ fontSize: '24px', color: 'darkgreen', fontWeight: 'bold' }}>{wine.price}€</p>
                <Rating initialRating={wine.rating} readonly />
            </div>
            <div className={styles.cardHalf}>

                <img src={wine.image_url} alt="Wine" />
            </div>

        </Link>
    );
};


export default WineCard;
