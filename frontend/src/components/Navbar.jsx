import { Link } from "react-router-dom"

export default function Navbar() {
  return (
    <nav style={{ padding: 16, borderBottom: "1px solid #ddd" }}>
      <Link to="/">Home</Link> |{" "}
      <Link to="/products">Products</Link> |{" "}
      <Link to="/cart">Cart</Link> |{" "}
      <Link to="/profile">Profile</Link>
    </nav>
  )
}
