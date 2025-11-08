// they can only view this page once they are authorized

export default function Layout({ children }: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        { children }
    );
}
