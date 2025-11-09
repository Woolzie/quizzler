"use client";
import React, { useEffect, useState } from "react";
import { handleJsonToCSV } from "../lib/convert.ts";
import { Error } from "./Error.tsx";
import { Loading } from "./Loading.tsx";

interface ShowTableType {
    serverData: Array<Array<string>>;
    currentView: number;
}

export const ShowTable = ({ serverData, currentView }: ShowTableType) => {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        const getServerData = new Promise((resolve, reject) => {
            let times = 0;
            setInterval(() => {
                times += 1;
                if (times > 30) reject();
                if (serverData[currentView] !== null) {
                    setLoading(false);
                    resolve(serverData[currentView]);
                }
            }, 100);
        });

        if (serverData[currentView] !== null) setLoading(false);
        else {
            setLoading(true);
            getServerData.catch(() => {
                setError(true);
            });
        }
    }, [currentView]);
    useEffect(() => {
        console.log("moew");
        setLoading(true);
    }, [currentView]);

    return (
        <>
            {error ? <Error /> : loading ? <Loading /> : (
                <Table
                    serverData={serverData[currentView]}
                />
            )}
        </>
    );
};

interface TableType {
    serverData: Array<string>;
}
const Table = ({ serverData }: TableType) => {
    const [cols, setCols] = useState(1);
    return (
        <div className={`w-[45%] grid grid-cols-${cols} gap-4`}>
            {serverData.map((row) =>
                row.map((val) => <div key={crypto.randomUUID()}>{val}</div>)
            )}
        </div>
    );
};
