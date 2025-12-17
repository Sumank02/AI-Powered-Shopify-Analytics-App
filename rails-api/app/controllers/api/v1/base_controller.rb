module Api
    module V1
      class BaseController < ActionController::API
        before_action :set_default_format
  
        rescue_from StandardError, with: :handle_internal_error
        rescue_from ActionController::ParameterMissing, with: :handle_bad_request
  
        private
  
        def set_default_format
          request.format = :json
        end
  
        def handle_internal_error(exception)
          render json: { error: "Internal Server Error", details: exception.message }, status: 500
        end
  
        def handle_bad_request(exception)
          render json: { error: "Bad Request", details: exception.message }, status: 400
        end
      end
    end
  end
  