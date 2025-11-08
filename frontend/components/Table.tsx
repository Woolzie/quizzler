"use client";
import React, { useEffect, useState } from "react";

import { usePapaParse } from "react-papaparse";
interface ITable {
    serverData: any;
    currentView: number;
}

export const Table = ({ serverData, currentView }: ITable) => {
    const [tableData, setTableData] = useState(null);
    const [loading, setLoading] = useState(true);

    const { jsonToCSV } = usePapaParse();
    //needs to be a promise around serverData
    //

    useEffect(() => {
        console.log(`${serverData}`);

        const handleJsonToCSV = (data) => {
            const results = jsonToCSV(data);
            const rows = results.split("\r");
            const arr: Array<string> = [];
            for (const row of rows) {
                console.log(row.split(","));
                arr.push(row.split(","));
            }
            return arr;
        };
        // ensures its not null
        if (serverData[1]) {
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
            {loading
                ? tableData[currentView].map((data) => <p>data</p>)
                : <p>meow</p>}
        </div>
    );
};
