import { Link } from "react-router-dom"

export default function ProductCard({ product }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: 12 }}>
      <h3>{product.name}</h3>
      <p>${product.price}</p>
      <Link to={`/product/${product.id}`}>View</Link>
    </div>
  )
}
