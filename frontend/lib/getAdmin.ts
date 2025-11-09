const apis = ["students", "faculty", "departments"];
const token =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI3NTU0NjAsInBheWxvYWQiOiIwNWFjODU5NC1mOTY2LTRhODQtODE1Ny1hMTZmYWRhNTIzY2UifQ.UjYgaXJJkZPEM9anr1Z8EGUaL8ZkjDE0vuRQwweH-uk";

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
