"use client";
import React, { useEffect, useState } from "react";

import { usePapaParse } from "react-papaparse";
interface IShowTable {
    serverData: any;
    currentView: number;
}

export const ShowTable = ({ serverData, currentView }: ITable) => {
    const [tableData, setTableData] = useState("");
    const [loading, setLoading] = useState(true);

    const { jsonToCSV } = usePapaParse();
    //needs to be a promise around serverData
    //

    useEffect(() => {
        const handleJsonToCSV = (data) => {
            console.log(`${data}`);
            if (data) {
                const results = jsonToCSV(data);
                const rows = results.split("\r");
                const arr: Array<string> = [];
                for (const row of rows) {
                    arr.push(row.split(","));
                }
                return arr;
            }
        };
        if (serverData) {
            setTableData((tableData) =>
                handleJsonToCSV(serverData[currentView])
            );
        }
    }, [serverData]);
    useEffect(() => {
        if (tableData && tableData[currentView]) setLoading(false);
    }, [tableData]);

    return (
        <div className="grid">
        </div>
    );
};
const Table = () => {
    return (
        <div className="grid">
        </div>
    );
};

const Loading = () => {
    //TODO: add some loading animation
    return <p>Loading...</p>;
};
