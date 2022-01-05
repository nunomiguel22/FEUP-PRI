import React, { useEffect, useState } from 'react';
import CSS from 'csstype';
import WineCard from '../components/wineCard';
import { Wine } from '../interfaces';
import { getQuery } from '../api/api';
import Footer from '../components/footer';

const Home: React.FC = () => {

    const [wineData, setWineData] = useState<Wine[]>([]);

    useEffect(() => {
        getQuery("note:excellent chicken~5^50",100,"OR").then(response => {
            setWineData(response.response.docs);
        });
    }, []);

    return (
        <div>
            <div style={cardGallery}>
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
            <Footer />
        </div>
    );
};

const cardGallery: CSS.Properties = {
    backgroundColor: '#EEEEEEEE',
    paddingBottom: '10px',
    paddingTop: '10px',
    margin: '50px 50px 50px 50px',
    borderRadius: '13px',
};

export default Home;