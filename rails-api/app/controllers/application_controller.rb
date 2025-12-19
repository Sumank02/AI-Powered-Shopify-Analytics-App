class ApplicationController < ActionController::Base
  # Allow serving HTML pages (not just JSON)
  protect_from_forgery with: :exception
end

