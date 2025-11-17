"use client";
import { ViewButton } from "@/components/ViewButton";
import { useEffect, useState } from "react";
import CSVReader from "../../components/Csv.tsx";
import { ShowTable } from "@/components/Table.tsx";

export default function AdminPage() {
    const [currentView, setView] = useState(0);

    return (
        <div className="w-screen h-full flex items-center flex-col justify-between">
            <ViewButton
                currentView={currentView}
                setView={setView}
            />
            <ShowTable currentView={currentView} />
        </div>
    );
}
