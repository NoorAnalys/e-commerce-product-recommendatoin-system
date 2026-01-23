import { useParams } from "react-router-dom"
import { products } from "../data/mockData"
import RecommendationSection from "../components/RecommendationSection"

export default function ProductDetail() {
  const { id } = useParams()
  const product = products.find(p => p.id === Number(id))

  if (!product) return <p>Product not found</p>

  return (
    <div style={{ padding: 20 }}>
      <h1>{product.name}</h1>
      <p>Price: ${product.price}</p>
      <button>Add to cart</button>
      <RecommendationSection />
    </div>
  )
}
