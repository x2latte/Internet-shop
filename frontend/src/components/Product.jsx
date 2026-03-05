import { Link } from 'react-router-dom';
import { Rating, Star } from '@smastrom/react-rating';

const myStyles = {
  itemShapes: Star,
  activeFillColor: '#ffb700',
  inactiveFillColor: '#fbf1a9',
};

export default function Product({ product }) {
  return (
    <div className="text-center flex flex-1 flex-col justify-between">
      <div>
        <Link to={`product/${product.id}`}>
          <div className="text-center">
            <img
              src={product.image}
              className="img-fluid w-auto h-auto mx-auto"
              alt={product.name}
            />
          </div>
        </Link>
        </div>
        <div>
          <h1 className="text-xl font-semibold">{product.name}</h1>

          <Rating
            value={product.rating}
            readOnly={true}
            itemStyles={myStyles}
            style={{ maxWidth: 200 }}
          />

          <h1 className="text-right text-lg font-semibold">{product.price} рублей</h1>
      </div>
    </div>
  );
}
