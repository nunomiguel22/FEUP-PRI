import React, { useEffect, useState } from 'react';
import CSS from 'csstype';
import WineCard from '../components/wineCard';
import { Wine } from '../interfaces';
import { getQuery } from '../api/api';
import PageLayout from '../components/pageLayout';


const Home: React.FC = () => {

    const [wineData, setWineData] = useState<Wine[]>([]);
    const [search, setSearch] = useState<string>('*');
    const [rows, setRows] = useState<number>(10);

    useEffect(() => {
        getQuery("note:\"" + search + "\"", rows, "OR").then(response => {
            setWineData(response.response.docs);
        });
    }, [search,rows]);

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
                    <input style={rowSelection}
                        type="number"
                        placeholder="Results"
                        value={rows}
                        min="0"
                        onChange={(e) => setRows(e.target.valueAsNumber)}
                    />
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