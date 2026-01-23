import { products } from "../data/mockData"
import ProductCard from "../components/ProductCard"

export default function Products() {
  return (
    <div style={{ padding: 20 }}>
      <h1>Products</h1>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 12 }}>
        {products.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  )
}
