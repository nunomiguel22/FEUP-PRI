import React, { useEffect, useState } from 'react';
import CSS from 'csstype';
import WineCard from '../components/wineCard';
import { Wine } from '../interfaces';
import { getQuery } from '../api/api';
import PageLayout from '../components/pageLayout';
import styles from '../styles/home.module.css';

const Home: React.FC = () => {

    const [wineData, setWineData] = useState<Wine[]>([]);
    const [search, setSearch] = useState<string>('');

    useEffect(() => {
        const q = search != '' ? "note:\"" + search + "\"" : '*';
        const q_sort = 'rating desc'
        getQuery(q, 100, "OR", q_sort).then(response => {
            setWineData(response.response.docs);
        });
    }, [search]);

    return (
        <PageLayout>
            <div className={styles.cardGallery}>
                <div className={styles.searchSection}>
                    <input className={styles.searchBar}
                        type="text"
                        placeholder="Search for a specific wine"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
                    <p>Results:{wineData.length}</p>
                </div>
                {
                    wineData.length === 0 ? (
                        <p> A carregar... </p>
                    ) : (
                        wineData.map(list =>
                            list ? (
                                <WineCard key={list.id} wine={list} />
                            ) : null,
                        )
                    )
                }
            </div>
        </PageLayout>
    );
};



export default Home;