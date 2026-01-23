import { Link } from "react-router-dom"

export default function ProductCard({ product }) {
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <p>${product.price}</p>
      <Link to={`/product/${product.id}`}>View</Link>
    </div>
  )
}
