import axios from 'axios';

const SOLR_API = axios.create({
    baseURL: "http://localhost:8983/solr/wines"
});

export const getQuery = async (q: string) => {
    try {
        const response = await SOLR_API.get('select', {
            params: { q },
        });
        return response.data;
    } catch (error) {
        console.error(error);
    }
};


export default SOLR_API;