"use client";
import Link from "next/link";
import "./../styles/dashboard.css";
interface CardProps {
    handleClick: React.MouseEventHandler<HTMLButtonElement>;
    header: string;
    content: string;
}
export default function Card(
    { handleClick, header, content }: CardProps,
) {
    return (
        <div className="w-[35%] h-[30%] card ">
            <h1>{header}</h1>
            <div className="flex flex-col justify-around items-center h-[75%] ">
                <p>{content}</p>
                <Link href={`/${header.toLowerCase()}/auth`}>
                    <button onClick={handleClick}>Log in</button>
                </Link>
            </div>
        </div>
    );
}
