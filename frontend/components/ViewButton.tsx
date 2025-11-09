import "@/styles/dashboard.css";
import { users } from "../lib/users.ts";
import { useEffect } from "react";
type IViewButton = {
    currentView: number;
    setView: React.Dispatch<React.SetStateAction<number>>;
};

export const ViewButton = ({ currentView, setView }: IViewButton) => {
    const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
        const value = Number(e.currentTarget.value);
        setView(value);
    };
    return (
        <div className="w-[40%] flex justify-center m-4 ">
            <div
                className="border flex justify-center basis-full border-card-border"
                style={{
                    borderRadius: "1rem",
                }}
            >
                {users.map((user, index) => (
                    <button
                        type="button"
                        key={crypto.randomUUID()}
                        value={index}
                        className="bg-pink-100 p-4 flex-1"
                        onClick={handleClick}
                        style={{
                            borderColor: "inherit",
                            backgroundColor: currentView === index
                                ? "yellow"
                                : "",
                            borderRight: index === 1 ? "1px solid" : "",
                            borderLeft: index === 1 ? "1px solid" : "",

                            borderBottomLeftRadius: index === 0 ? "1rem" : "",
                            borderTopLeftRadius: index === 0 ? "1rem" : "",
                            borderTopRightRadius: index === 2 ? "1rem" : "",
                            borderBottomRightRadius: index === 2 ? "1rem" : "",
                        }}
                    >
                        {user}
                    </button>
                ))}
            </div>
        </div>
    );
};
