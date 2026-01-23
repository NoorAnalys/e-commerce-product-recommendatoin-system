import { products } from "../data/mockData"
import ProductCard from "../components/ProductCard"
import RecommendationSection from "../components/RecommendationSection"

export default function Home() {
  return (
    <div className="page">
      <h1>Home</h1>
      <div className="product-grid">
        {products.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
      <RecommendationSection />
    </div>
  )
}
