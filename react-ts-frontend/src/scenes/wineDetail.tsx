import React, { useEffect, useState } from 'react';
import PageLayout from '../components/pageLayout';
import { Wine } from '../interfaces';
import { useParams } from "react-router-dom";
import { getQuery } from '../api/api';

const WineDetail: React.FC = () => {
    const id = useParams()?.id;

    const [wine, setWine] = useState<Wine>();

    useEffect(() => {
        getQuery("id:" + id).then(response => {
            setWine(response.response.docs[0]);
        });
    }, []);
    console.log(wine?.note);
    return (
        <PageLayout>
            <h1>{wine?.name}</h1>
            {

                wine?.note.map(list =>
                    list ? (
                        <p>{list}</p>

                    ) :
                        null)
            }
        </PageLayout>
    );
};


export default WineDetail;