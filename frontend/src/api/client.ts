import axios from "axios";

console.log("Mi API URL es:", import.meta.env.VITE_API_URL);
const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export default apiClient;
