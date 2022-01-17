import React, { useEffect, useState } from 'react';
import PageLayout from '../components/pageLayout';
import { Wine } from '../interfaces';
import { useParams } from "react-router-dom";
import { getQuery } from '../api/api';
import styles from '../styles/wine.module.css';
import Rating from 'react-rating';

const WineDetail: React.FC = () => {
    const id = useParams()?.id;

    const [wine, setWine] = useState<Wine>();

    useEffect(() => {
        getQuery("id:" + id).then(response => {
            setWine(response.response.docs[0]);
        });
    }, []);

    return (
        <PageLayout>

            <div>
                <div className={styles.imgSection}>
                    <img src={wine?.image_url} alt="Wine" />

                </div>
                <div className={styles.infoSection}>
                    <h1 style={{ marginTop: '0' }}>{wine?.name}</h1>
                    <h5 style={{ color: '#616161' }}>{wine?.winery}</h5>
                    <p style={{ fontSize: '17px' }}>{wine?.region}, {wine?.country}</p>
                    <Rating initialRating={wine?.rating} readonly />
                    <p style={{ fontSize: '24px', color: 'darkgreen', fontWeight: 'bold' }}>{wine?.price}€</p>

                </div>

                <div className={styles.reviewSection}>
                    <h1 className={styles.reviewTitle}>Reviews</h1>
                    {

                        wine?.note.map(list =>
                            list ? (
                                <p className={styles.review}>{list}</p>

                            ) :
                                null)
                    }
                </div>



            </div>





        </PageLayout>
    );
};


export default WineDetail;