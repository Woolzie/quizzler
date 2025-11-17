"use client";
import React, { useEffect, useRef, useState } from "react";
import { Error } from "./Error.tsx";
import { Loading } from "./Loading.tsx";

import { adminGetRequest } from "@/lib/getAdmin.ts";
import { handleJsonToCSV } from "@/lib/convert.ts";
import { usePapaParse } from "react-papaparse";

interface ShowTableType {
    currentView: number;
}

export const ShowTable = ({ currentView }: ShowTableType) => {
    const [loading, setLoading] = useState([true, true, true]);
    const [error, setError] = useState(false);

    const [serverData, setServerData] = useState(new Array(3).fill(null));
    const { jsonToCSV } = usePapaParse();

    //TODO: loading didnt work for shit when the serverData was null
    useEffect(() => {
        function getTableValues() {
            if (serverData[currentView] === null) {
                loading[currentView] = true;
                setLoading([...loading]);
                const res = adminGetRequest(currentView);
                res.then((value) => {
                    const csvData = handleJsonToCSV(jsonToCSV, value);
                    serverData[currentView] = csvData;
                    setServerData((serverData) => [...serverData]);
                    console.log(serverData[currentView]);
                    loading[currentView] = false;
                    setLoading([...loading]);
                });
                res.catch(() => setError(true));
            }
        }

        getTableValues();
    }, [currentView]);
    //TODO: do something with error

    return (
        <>
            {error ? <Error /> : serverData[currentView]
                ? (
                    <>
                        <Table
                            serverData={serverData[currentView]}
                        />
                        <CreateButton />
                    </>
                )
                : <Loading />}
        </>
    );
};

const CreateButton = (setServerData) => {
    const [view, setView] = useState(false);
    const firstRef = useRef(null!);
    const handleClick = () => {
        // toogles the sight of another component
        setView(!view);
    };
    return (
        <div className="flex items-center flex-col">
            {view && <InputFields ref={firstRef} />}
            <button
                className="p-4 m-4 bg-slate-300 rounded-3xl"
                onClick={handleClick}
            >
                Create
            </button>
        </div>
    );
};

const InputFields = ({ firstRef }) => {
    const [data, setData] = useState({ first: "", second: "" });
    //secondRef for the sake of symmetry

    const handleInput = (e: React.InputEventHandler<HTMLInputElement>) => {
        setData({ ...data, [e.currentTarget.name]: e.currentTarget.value });
    };

    const inputDesign = "mt-4 m-2 border-2 border-slate-200";
    return (
        <div>
            <input
                type="text"
                name="first"
                ref={firstRef}
                onInput={handleInput}
                className={inputDesign}
            />

            <input
                type="text"
                name="second"
                onInput={handleInput}
                className={inputDesign}
            />
        </div>
    );
};

interface TableType {
    serverData: Array<string>;
}

const Table = ({ serverData }: TableType) => {
    const [cols, _] = useState(serverData[0].length);
    useEffect(() => {
        console.log(cols);
    });

    return (
        <div
            className={`w-[45%] grid grid-cols-${cols} gap-1 border-4 border-stone-950  text-center bg-black`}
        >
            {serverData.map((row, index) =>
                row.map((val) => (
                    <div
                        key={crypto.randomUUID()}
                        className="p-3"
                        style={{
                            background: index ? "white" : "black",
                            color: index ? "black" : "white",
                        }}
                    >
                        {val}
                    </div>
                ))
            )}
        </div>
    );
};
