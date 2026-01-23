import { recommendations } from "../data/mockData"
import ProductCard from "./ProductCard"

export default function RecommendationSection() {
  return (
    <div className="recommendations">
      <h2>Recommended for you</h2>
      <div className="product-grid">
        {recommendations.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  )
}
