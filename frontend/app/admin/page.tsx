"use client";
import { ViewButton } from "@/components/ViewButton";
import { useEffect, useState } from "react";
import CSVReader from "../../components/Csv.tsx";
import { Table } from "@/components/Table.tsx";

export default function AdminPage() {
    const [currentView, setView] = useState(0);
    const [inputCsv, setInputCsv] = useState(null);
    // array of json data from all the users get requests
    const [serverData, setServerData] = useState(new Array(3));
    //
    //TODO: once inputcsv is set, call useEffect and hit the api

    useEffect(() => {
        const apis = ["students", "faculty", "departments"];
        const token =
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI2NDAxNzEsInBheWxvYWQiOiIwNWFjODU5NC1mOTY2LTRhODQtODE1Ny1hMTZmYWRhNTIzY2UifQ.ooZOOKP1Asu_rwd6b3nouTlPIG93wU5-eLwHUuRz97k";
        const PromiseGetAll = new Promise((resolve, reject) => {
            apis.forEach(async (api, index) => {
                const url = `http://localhost:8000/api/v1/admin/get_${api}/`;
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
                res.then((val) => {
                    serverData[index] = val;
                    //TODO: find a more elegant solution to make the promise wait for the forEach loop to finish executing
                    if (index === 2) {
                        resolve(serverData);
                    }
                });
            });
        });
        PromiseGetAll.then((data) =>
            setServerData((serverData) => [...serverData]) || console.log(data)
        );
        if (inputCsv) {
            // hit the create_{api} endpoints
            // after that, call getAll
        }
    }, [inputCsv]);

    //BUG: no dependency list or serverData in dependency list causes it to call itself a billion times

    return (
        <div className="w-screen h-full flex items-center flex-col justify-between">
            <ViewButton
                currentView={currentView}
                setView={setView}
            />
            <Table serverData={serverData} currentView={currentView} />
            <CSVReader setInputCsv={setInputCsv} />
        </div>
    );
}
