"use client";
import { ViewButton } from "@/components/ViewButton";
import { useEffect, useState } from "react";
import CSVReader from "../../components/Csv.tsx";
import { ShowTable } from "@/components/Table.tsx";
import { adminGetRequest } from "../../lib/getAdmin.ts";
import { handleJsonToCSV } from "@/lib/convert.ts";
import { usePapaParse } from "react-papaparse";

export default function AdminPage() {
    const [currentView, setView] = useState(0);
    const [inputCsv, setInputCsv] = useState(null);
    // this has to be in csv format
    const [serverData, setServerData] = useState(new Array(3).fill(null));
    const { jsonToCSV } = usePapaParse();

    useEffect(() => {
        function getTableValues() {
            if (serverData[currentView] === null) {
                const res = adminGetRequest(currentView);
                res.then((value) => {
                    const csvData = handleJsonToCSV(jsonToCSV, value);
                    serverData[currentView] = csvData;
                    setServerData((serverData) => [...serverData]);
                });
                console.log(serverData);
            }
        }
        getTableValues();
    }, [currentView]);

    useEffect(() => {
        if (inputCsv) {
            // hit the create_{api} endpoints
        }
    }, [inputCsv]);

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
