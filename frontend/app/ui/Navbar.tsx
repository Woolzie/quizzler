"use client";
import { Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";
import "@/styles/navbar.css";

const Navbar = () => {
    const [lightMode, setLightMode] = useState<boolean>(
        null!,
    );
    useEffect(() => {
        if (lightMode === null) {
            setLightMode(document.body.classList.contains("dark"));
        }
    });

    return (
        <div className="w-screen h-[5vh] flex justify-between navbar items-center ">
            <div className=""></div> {/* throw away  */}
            <div
                className="flex justify-center items-center text-white bg-black  size-fit  rounded-full mr-4 "
                onClick={() => {
                    document.body.classList.toggle("dark");
                    setLightMode(!lightMode);
                }}
            >
                <div className="p-2">{lightMode ? <Sun /> : <Moon />}</div>
            </div>
        </div>
    );
};
export { Navbar };
