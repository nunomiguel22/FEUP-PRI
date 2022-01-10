import React, { useEffect, useState } from 'react';
import CSS from 'csstype';
import WineCard from '../components/wineCard';
import { Wine } from '../interfaces';
import { getQuery } from '../api/api';
import PageLayout from '../components/pageLayout';

const Home: React.FC = () => {

    const [wineData, setWineData] = useState<Wine[]>([]);
    const [search, setSearch] = useState<string>('*');

    useEffect(() => {
        getQuery("note:" + search + "~5^50", 100, "OR").then(response => {
            setWineData(response.response.docs);
        });
    }, [search]);



    return (
        <PageLayout>
            <div style={cardGallery}>
                <div style={searchSection}>
                    <input style={searchBar}
                        type="text"
                        placeholder="Search for a specific wine"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
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

const cardGallery: CSS.Properties = {
    paddingBottom: '10px',
    paddingTop: '10px',
    borderRadius: '13px',
};

const searchSection: CSS.Properties = {
    textAlign: 'center',
};

const searchBar: CSS.Properties = {
    backgroundColor: '#EEEEEE',
    boxShadow: '1px 1px #888888',
    padding: '6px',
    border: 'none',
    fontSize: '17px',
    width: '50%',
};

export default Home;