// import "@/styles/navbar.css";
const Navbar = () => {
    return (
        <div className="w-screen flex justify-between bg-navbar p-2">
            {/*TODO: this could be the theme change button */}
            <div className=""></div>
            <div className="p-1 bg-navitems rounded-full">
                <button className="p-3 menu-icon "></button>
            </div>
        </div>
    );
};
export { Navbar };
