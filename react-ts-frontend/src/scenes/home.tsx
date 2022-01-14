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
        getQuery(q, 100, "OR").then(response => {
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
<<<<<<< HEAD
                    <input style={rowSelection}
                        type="number"
                        placeholder="Results"
                        value={rows}
                        min="0"
                        onChange={(e) => setRows(e.target.valueAsNumber)}
                    />
=======
                    <p>Results:{wineData.length}</p>
>>>>>>> 54bf39503bc81cb9fcabf9da291882fb8055dc83
                </div>
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
        </PageLayout>
    );
};

<<<<<<< HEAD
const cardGallery: CSS.Properties = {
    paddingBottom: '10px',
    paddingTop: '10px',
    borderRadius: '13px',
};

const searchSection: CSS.Properties = {
    textAlign: 'center',
    margin:'0 auto 0 auto'
};

const searchBar: CSS.Properties = {
    backgroundColor: '#EEEEEE',
    boxShadow: '1px 1px #888888',
    padding: '6px',
    border: 'none',
    fontSize: '17px',
    width: '60%',
    float:'left'
};
=======

>>>>>>> 54bf39503bc81cb9fcabf9da291882fb8055dc83

const rowSelection: CSS.Properties = {
    backgroundColor: '#EEEEEE',
    boxShadow: '1px 1px #888888',
    padding: '6px',
    border: 'none',
    fontSize: '17px',
    width: '15%',
    float:'left',
    marginLeft:'10px'
};


export default Home;