class HomeController < ApplicationController
  def index
    # Serve the main application page
    render 'home/index', layout: 'application'
  end
end

