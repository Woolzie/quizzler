"use client";
import { ViewButton } from "@/components/ViewButton";
import { useEffect, useState } from "react";
import CSVReader from "../../components/Csv.tsx";
import { ShowTable } from "@/components/Table.tsx";

export default function AdminPage() {
    const [currentView, setView] = useState(0);
    const [inputCsv, setInputCsv] = useState(null);
    // array of json data from all the users get requests
    const [serverData, setServerData] = useState(null);

    useEffect(() => {
        const apis = ["students", "faculty", "departments"];
        const token =
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI2NDY0MTQsInBheWxvYWQiOiIwNWFjODU5NC1mOTY2LTRhODQtODE1Ny1hMTZmYWRhNTIzY2UifQ.7HuFwrKKJxMQwi57yYSOaZTnqgCmD1NvijYg2LXQvzI";
        //TODO: find a more elegant solution to make the promise wait for the forEach loop to finish executing

        const createPromises = new Promise((resolve, reject) => {
            //ensure this runs before the promise.all
            const promises = new Array(3).fill(null);
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
                promises[index] = res;
                // this is retarded
                //TODO: once the rest arent null, update serverData aswell
                if (promises[currentView]) resolve(promises);
            });
        });

        createPromises.then((promises) => Promise.all(promises)).then((
            results,
        ) => {
            console.log(results);
            setServerData((serverData) => results);
        });
        if (inputCsv) {
            // hit the create_{api} endpoints
        }
    }, [inputCsv]);

    //BUG: no dependency list or serverData in dependency list causes it to call itself a billion times

    return (
        <div className="w-screen h-full flex items-center flex-col justify-between">
            <ViewButton
                currentView={currentView}
                setView={setView}
            />
            <ShowTable serverData={serverData} currentView={currentView} />
            <CSVReader setInputCsv={setInputCsv} />
        </div>
    );
}
