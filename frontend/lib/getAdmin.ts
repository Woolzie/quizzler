const apis = ["students", "faculty", "departments"];
const token =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjMyOTY1ODgsInBheWxvYWQiOiIwNWFjODU5NC1mOTY2LTRhODQtODE1Ny1hMTZmYWRhNTIzY2UifQ.ulIyk6dBLD42JcLYjecBKPnKM4lTRUGsWDsErrv_060";

async function adminGetRequest(currentView) {
    const url = `http://localhost:8000/api/v1/admin/get_${apis[currentView]}/`;
    const fetchResponse = await fetch(url, {
        method: "GET",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
            "Access-Control-Allow-Origin": "*",
        },
    });
    const res = fetchResponse.json();
    return res;
}
export { adminGetRequest };
