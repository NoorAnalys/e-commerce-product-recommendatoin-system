import { recommendations } from "../data/mockData"
import ProductCard from "./ProductCard"

export default function RecommendationSection() {
  return (
    <div>
      <h2>Recommended for you</h2>
      <div style={{ display: "flex", gap: 12 }}>
        {recommendations.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  )
}
