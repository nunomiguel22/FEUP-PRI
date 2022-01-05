import React from 'react';
import { Wine } from '../interfaces';
import styles from '../styles/winecard.module.css';
import { Link } from "react-router-dom";
interface Props {
    wine: Wine;
}

const WineCard: React.FC<Props> = ({ wine }: Props) => {
    return (
        <div className={styles.cardStyle}>
            <Link to={'/wine/' + wine.id}>{wine.name}</Link>
            <p>{wine.year}</p>
            <img src={wine.image_url} alt="Wine" />
        </div>
    );
};


export default WineCard;
