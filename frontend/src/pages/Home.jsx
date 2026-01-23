import { products } from "../data/mockData"
import ProductCard from "../components/ProductCard"
import RecommendationSection from "../components/RecommendationSection"

export default function Home() {
  return (
    <div style={{ padding: 20 }}>
      <h1>Home</h1>
      <div style={{ display: "flex", gap: 12 }}>
        {products.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
      <RecommendationSection />
    </div>
  )
}
